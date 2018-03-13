#!/usr/bin/env python

def _main():
    eurocars = [ 'volvo', 'saab', 'fiat', 'volkswagen' ]
    americars = [ 'ford', 'chevy', 'mazda', 'dodge' ]

    result = [ car for carorigin in [eurocars,americars] for car in carorigin if len(car) == 4 ]

#    result = []
#    for carorigin in [ eurocars, americars ]:
#        for car in carorigin:
#            if len(car) == 4:
#                result.append( car )

    print( '4 character cars: {}'.format(result) )
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit( _main() )
