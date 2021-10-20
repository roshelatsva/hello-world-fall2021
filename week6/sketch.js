let bubble1;
let bubble2;
let bgColor = 0;

function setup() {
  createCanvas(600, 400);
  bubble1 = new Bubble(width/2, height/2, 50);
  bubble2 = new Bubble(400, 200, 100);
  bgColor = color(random(255), random(255), random(255));
  
  
}


function draw() {
  background(0);
  noStroke();
  
  if (bubble1.intersects(bubble2)) {
  background(200, 0, 100);
  }

  bubble1.show();
  bubble2.show();
  bubble1.move();
  bubble2.x = mouseX;
  bubble2.y = mouseY; 
  
  
  if (mouseIsPressed){
    background(bgColor);
  }
}


function mousePressed(){
    let d = dist(mouseX, mouseY, width/2, height/2);
    if (d < 100){  
      bgColor = color(random(255), random(255), random(255));
  
  }
  // for (let i = 0; i < bubble1.length; i++){
  //   bubble1[i].clicked(mouseX, mouseY);
  //}
  // bgColor = random(255);
}


  




class Bubble {
  constructor(x, y, r = 50) {
    this.x = x;
    this.y = y;
    this.r = r;
    this.brightness = 0;
  }

  intersects(other) {
    let d = dist(this.x, this.y, other.x, other.y);
    return d < this.r + other.r;
  }

  changeColor(bright) {
    this.brightness = bright;
  }

  contains(px, py) {
    let d = dist(px, py, this.x, this.y);
    if (d < this.r) {
      return true;
    } else {
      return false;
    }
  }
  
   move() {
    this.x = this.x + random(-1, 1);
    this.y = this.y + random(-1, 1);
   }   

  show() {
    stroke(255);
    strokeWeight(4);
    fill(this.brightness, 125);
    ellipse(this.x, this.y, this.r * 2);
  }
  
  click(px, py){
   let d = dist(px, py, this.x, this.y);
    if (d < this.r) {
      this.brightness = bgColor; 
  }
}
}  