#include <string>
#include <map>

using namespace std;
#ifndef LSystem_H
#define LSystem_H

class LSystem{
public:
  LSystem();
  string rewriteSystem(string,string,string);//TODO make private
  string computeLSystem(string,int,string);//TODO should take an enum
  //to define production rule
private:
  map<char,string> rules;
};

#endif
