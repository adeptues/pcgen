#include "LSystem.hpp"

LSystem::LSystem(){
  this->rules['A'] = "AB";//TODO problems here
  this->rules['B'] = "A";
  this->rules['F'] = "F-F+F+F-F";
}
//myabe dont need rules
string LSystem::rewriteSystem(string seed,string acc,string rules){
  stringstream ss;
  if(seed.size() == 0){
    return acc;
  }else{
    string product;
    char head = seed[0];
    ss << head;//char to string
    ss >> product;
    if(this->rules.count(head) == 1){//TODO does not handle rules not
      product = this->rules.at(head);
    }
    string tail = seed.substr(1,seed.size());
    return rewriteSystem(tail,acc + product,rules);
  }
}

string LSystem::computeLSystem(string axiom,int n,string rule){
  //TODO investigate whether rules variable is needed
  if(n == 0){
    return axiom;
  }else{
    string acc = rewriteSystem(axiom,"","");
    return computeLSystem(acc,n-1,rule);
  }
}
