from mininet.topo import Topo

class MyTopo( Topo ):
    def build(self):
        self.addHost('hostA', ip='10.58.3.1/24')
        self.addHost('hostB', ip='10.58.3.3/24')
        self.addHost('hostC', ip='10.76.5.5/24')
        self.addHost('container1', ip='172.22.0.4/24')

        self.addLink('hostA', 'hostB')
        self.addLink('hostB', 'hostC', params1={'ip': '10.76.5.1/24'})
        self.addLink('hostA', 'container1', params1={'ip': '172.22.0.1/24'}, params2={'ip': '172.22.0.4/24'})

topos = { 'mytopo': MyTopo }

# vim: set ts=4 sw=4 expandtab ai :
