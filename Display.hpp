#include <wx/wx.h>

#include "enums.hpp"
#ifndef  DISPLAY_H
#define DISPLAY_H
class Display: public wxFrame{
  
 public:
    Display(const wxString& title, const wxPoint& pos, const wxSize& size);
private:
    void OnHello(wxCommandEvent& event);
    void OnExit(wxCommandEvent& event);
    void OnAbout(wxCommandEvent& event);
    wxDECLARE_EVENT_TABLE();

};
#endif
