""" This is an implementation of l stsrems"""
#!/usr/bin/python

import lsystem
import turtlerender



def main():
    ls = lsystem.Lsystem(lsystem.Lsystem.DRAGON)
    system = ls.compute_system_alt(10)
    tr = turtlerender.turtlerender()
    tr.draw(system)
    tr.exitonclick()

if __name__ == '__main__':
    main()
