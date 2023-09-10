## Running

To run this model, first start mininet:

```
sudo mn --custom topo.py --topo mytop
```

And then apply the routes and other configuration:

```
mininet> source config.mn
```

## Testing

Ping from the container to hostC:

```
mininet> container1 ping hostC
```
