#include <gtest/gtest.h>
#include <string>
#include <iostream>
#include "LSystem.hpp"
using namespace std;

TEST(LSystemTest,recursiveRewrite){
  LSystem lsys;
  string seed  = "AB";
  string expected = "ABA";
  string result = lsys.rewriteSystem(seed,"","");
  EXPECT_EQ(expected,result);
}

TEST(LSystemTest,testRwrite){
  LSystem lsys;
  string seed  = "A";
  string expected = "AB";
  string result = lsys.rewriteSystem(seed,"","");
  EXPECT_EQ(expected,result);
}

TEST(LSystemTest,testKochCurve){
  LSystem lsys;//Th
  string axiom  = "F";
  string expected = "F-F+F+F-F";
  int steps = 1;
  string result = lsys.computeLSystem(axiom,steps,"");
  EXPECT_EQ(expected,result);
}

TEST(LSystemTest,testKochCurve2){
  LSystem lsys;
  string axiom = "F";
  string expected = "F-F+F+F-F-F-F+F+F-F+F-F+F+F-F+F-F+F+F-F-F-F+F+F-F-F-F+F+F-F-F-F+F+F-F+F-F+F+F-F+F-F+F+F-F-F-F+F+F-F+F-F+F+F-F-F-F+F+F-F+F-F+F+F-F+F-F+F+F-F-F-F+F+F-F+F-F+F+F-F-F-F+F+F-F+F-F+F+F-F+F-F+F+F-F-F-F+F+F-F-F-F+F+F-F-F-F+F+F-F+F-F+F+F-F+F-F+F+F-F-F-F+F+F-F";
  int steps = 3;
  string result = lsys.computeLSystem(axiom,steps,"");
  EXPECT_EQ(expected,result);
}



int main(int argc, char **argv) {
  ::testing::InitGoogleTest( &argc, argv );
  return RUN_ALL_TESTS();
}

