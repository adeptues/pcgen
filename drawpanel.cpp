

#include "drawpanel.h"

DrawPanel::DrawPanel(wxFrame * parent){
    wxPanel(parent);//i guess equivelent to super
}
void DrawPanel::paintEvent(wxPaintEvent& evt)
{

}
void DrawPanel::paintNow()
{

}



BEGIN_EVENT_TABLE(DrawPanel, wxPanel)
// some useful events
/*
 EVT_MOTION(DrawPanel::mouseMoved)
 EVT_LEFT_DOWN(DrawPanel::mouseDown)
 EVT_LEFT_UP(DrawPanel::mouseReleased)
 EVT_RIGHT_DOWN(DrawPanel::rightClick)
 EVT_LEAVE_WINDOW(DrawPanel::mouseLeftWindow)
 EVT_KEY_DOWN(DrawPanel::keyPressed)
 EVT_KEY_UP(DrawPanel::keyReleased)
 EVT_MOUSEWHEEL(DrawPanel::mouseWheelMoved)
 */
 
// catch paint events
EVT_PAINT(DrawPanel::paintEvent)
 
END_EVENT_TABLE()