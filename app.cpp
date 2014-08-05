#include "App.hpp"

bool App::OnInit(){

  Display *frame = new Display( "Hello World", wxPoint(50, 50), wxSize(450, 340) );
 frame->Show( true );
    return true;
}



wxIMPLEMENT_APP(App);