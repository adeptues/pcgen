#include <wx/wxprec.h>
#ifndef WX_PRECOMP
#include <wx/wx.h>
#endif

#ifndef APP_H
#define APP_H

class App: public wxApp{
public:
  virtual bool OnInit();

};
wxIMPLEMENT_APP(App);
#endif
