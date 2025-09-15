import cv2
import numpy as np
import os
from flask import Flask,request,Response,render_template,url_for,send_file
app=Flask(__name__)
import cv2
import numpy as np

def videoStream(color):
    rem=color.lstrip("#")
    r=int(rem[0:2],16)
    g=int(rem[2:4],16)
    b=int(rem[4:6],16)
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        low = np.array([b,g,r])
        high = np.array([255,255,255])
        mask = cv2.inRange(hsv, low, high)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        output = frame.copy()

        for i, c in enumerate(contours):
            if cv2.contourArea(c) > 300:  
                cv2.drawContours(output, [c], -1, (0, 255, 0), 2)
                x, y, w, h = cv2.boundingRect(c)
                cv2.putText(output, f"Obj {i+1}", (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

      
        _, buffer = cv2.imencode(".jpg", output)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()
    cv2.destroyAllWindows()


@app.route("/st",methods=["GET","POST"])
def detect():
    if request.method=="GET":
     return render_template("video.html")
    else:
     color= request.form["color"]
     return Response(videoStream(color),mimetype='multipart/x-mixed-replace; boundary=frame')
    
    
def imagecol(color,path,fil):
    img=cv2.imread(path)
    rem=color.lstrip("#")
    r=int(rem[0:2],16)
    g=int(rem[2:4],16)
    b=int(rem[4:6],16)
    lower=np.array([b,g,r])
    upper=np.array([255,255,255])
    range=cv2.inRange(img,lower,upper)
    blur=cv2.GaussianBlur(range,(5,5),0)
    countour,hierachy=cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in countour]
    max_area = max(areas) if areas else 0
    for c in countour:
     if cv2.contourArea(c) > 0.2 * max_area:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    path1=os.path.join(os.getcwd(),"upload","img1.webp")
    cv2.imwrite(path1,img)
    return send_file(path1,as_attachment=True,mimetype="image/*")

@app.route("/image",methods=["GET","POST"])
def img():
    if request.method=="GET":
       return render_template("img.html")
    else:
        col=request.form["color"]
        file=request.files["image"]
        if col=="":
           return "colr not choosen"
        elif  file=="":
           return "no files selected"
        else :
           path=os.path.join(os.getcwd(),"upload",file.filename)
           file.save(path)
           return imagecol(col,path,file)

       
if __name__=='__main__':
   app.run(debug=True)
 
