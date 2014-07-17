#include "Turtle.hpp"

Turtle::Turtle(int x,int y,int distance,double angle){
  this->x = x;
  this->y = y;
  this->distance = distance;
  this->angle = angle;
  this->penState = true;
}

void Turtle::drawWord(string word){
  //grammar definition and what to do for each symbol
  
}

void Turtle::moveForward(){
  
}

void Turtle::turnLeft(){
  
}

void Turtle::turnRight(){
}
void Turtle::penUp(){
  this->penState = false;
}
void Turtle::penDown(){
  this->penState = true;
}
