#include <string>
using namespace std;

#ifndef TURTLE_H
#define TURTLE_H

class Turtle {
public:
  Turtle(int x,int y,int distance, double angle);
  //need window referecnce to draw on
  void drawWord(string word);
  void moveForward();
  void turnRight();
  void turnLeft();
  void penUp();
  void penDown();
private:
  int x,y,distance;
  double angle;
  bool penState;//TODO better name
};

#endif
