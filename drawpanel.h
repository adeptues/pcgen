
#ifndef DRAWPANEL_H
#define DRAWPANEL_H

#include <wx/wx.h>
#include "Turtle.hpp"

class DrawPanel :  wxPanel
{
public:
  DrawPanel(wxFrame * parent);
  void paintEvent(wxPaintEvent& evt);
  void paintNow();
  
   // some useful events
    /*
     void mouseMoved(wxMouseEvent& event);
     void mouseDown(wxMouseEvent& event);
     void mouseWheelMoved(wxMouseEvent& event);
     void mouseReleased(wxMouseEvent& event);
     void rightClick(wxMouseEvent& event);
     void mouseLeftWindow(wxMouseEvent& event);
     void keyPressed(wxKeyEvent& event);
     void keyReleased(wxKeyEvent& event);
     */
    DECLARE_EVENT_TABLE()
private:
  Turtle turtle;
};

#endif // DRAWPANEL_H
