#!/usr/bin/env python

def add_2( a, b ):
#    print( 'adding {} and {}'.format(a,b) )
    return a + b


def _main():
    inputs = range(1, 11)
    results = []
    for a,b in  zip( inputs, inputs[1:] ):
        results.append( add_2(a,b) )
    print( 'doing something with results...' )
    # pretend I'm doing something with results
    return 0


if __name__ == '__main__':
    import sys
    sys.exit( _main() )


