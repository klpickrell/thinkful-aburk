#!/usr/bin/env python

def _main():
    eurocars = [ 'volvo', 'saab', 'fiat', 'volkswagen' ]
    americars = [ 'ford', 'chevy', 'mazda', 'dodge' ]

    result = []
    for car in eurocars:
        if len(car) == 4:
            result.append( car )
    for car in americars:
        if len(car) == 4:
            result.append( car )

    print( '4 character cars: {}'.format(result) )
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit( _main() )
