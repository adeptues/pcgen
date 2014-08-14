""" This is an implementation of l stsrems"""
#!/usr/bin/python

import lsystem
import turtlerender



def main():
    ls = lsystem.Lsystem(lsystem.Lsystem.F_PLANT)
    system = ls.compute_system_alt(4)
    tr = turtlerender.turtlerender(angle = 22.5)
    tr.draw(system)
    tr.exitonclick()

if __name__ == '__main__':
    main()
