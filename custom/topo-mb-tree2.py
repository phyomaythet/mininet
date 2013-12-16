# Topo-mb-tree2.py
'''
'''

from mininet.topo import Topo


class MiddleBoxTopo(Topo):
    """
    Simple middlebox test topology.
    """

    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        #Add hosts, middleboxes and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        mb = self.addMiddleBox( 'm1' )
        topSwitch = self.addSwitch( 's1' )
        leftSwitch = self.addSwitch( 's2' )
        rightSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( topSwitch, leftSwitch )
        self.addLink( topSwitch, rightSwitch )
        self.addLink( leftSwitch, leftHost )
        self.addLink( leftSwitch, rightHost )
        self.addLinkPair( rightSwitch, mb )

topos = { 'mbtopo': ( lambda: MiddleBoxTopo() ) }

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
