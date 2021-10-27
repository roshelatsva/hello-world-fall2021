var capture;
var tracker;
var w = 640;
var h = 480;

// Arrays for the position #'s of each part of a Face
var rEye = [23, 63, 24, 64];
var lEye = [30, 68, 29, 67];
var rEyebrow = [19, 20, 21, 22];
var lEyebrow = [15, 16, 17, 18];
var rPupil = [27];
var lPupil = [32];
var uLip = [45, 46, 47, 48, 49, 50];
var bLip = [44, 56, 57, 58, 50, 51];
var positions = []; 

var emojiSize = 20;

function setup() {
    capture = createCapture(VIDEO);
    createCanvas(w, h);
    capture.size(w, h);
    capture.hide();

    tracker = new clm.tracker();
    tracker.init();
    tracker.start(capture.elt);
}

function draw() {
    image(capture, 0, 0, w, h);

    positions = tracker.getCurrentPosition();

    if (positions.length > 0) {
     
        drawFaceComponentEmoji(lEye, "👁");
        drawFaceComponentEmoji(rEye, "👁");

 
        drawFaceComponentEmoji(rEyebrow, "🍀");
        drawFaceComponentEmoji(lEyebrow, "🌸");

       
        drawFaceComponentEmoji(uLip, "👄");
        drawFaceComponentEmoji(bLip, "💋");

        drawFaceComponentEmoji(rPupil, "🔥");
        drawFaceComponentEmoji(lPupil, "🔥");
    }

}


function drawFaceComponentEmoji(componentPoints, emojiString = "😀"){
    // pupils only
    textSize(emojiSize);
    textAlign(CENTER, CENTER); // Draw from middle
    for (var i = 0; i < componentPoints.length; i++) {
        var index = componentPoints[i];
        text(emojiString, positions[index][0], positions[index][1]);
    }
}