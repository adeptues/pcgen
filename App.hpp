#include <wx/wx.h>
#include <memory>
#include "Display.hpp"
#include "enums.hpp"

using namespace std;
#ifndef APP_H
#define APP_H

class App: public wxApp{
public:
  virtual bool OnInit();

};

#endif
