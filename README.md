# Uber-ride-sharing-simulation
A computer model simulates ride-sharing service to see the effect of different scenarios.

## Getting Started

### Prerequisites

* Python 3.x
* Terminal (in Unix) OR PowerShell (in Windows)

### Download and run the simulation
```
# Change to HOME directory
$ cd ~

# Clone this repo and 'cd' into it
$ git clone https://github.com/jellycsc/Uber-ride-sharing-simulation.git
$ cd Uber-ride-sharing-simulation/

# Let's start simulation
$ python3 simulation.py
```

## Small Example
```
Events file: events_small.txt
1 -- Dan: Request a driver
10 -- Arnold: Request a rider
12 -- Arnold: Pickup Dan
16 -- Dan: Cancel request
17 -- Arnold: Dropoff Dan
17 -- Arnold: Request a rider
{'driver_ride_distance': 10.0, 'driver_total_distance': 14.0, 'rider_wait_time': 11.0}
```
Compare with the sample [output](output_small.txt):
```
1 -- Dan: Request a driver
10 -- Arnold: Request a rider
12 -- Arnold: Pickup Dan
16 -- Dan: Cancel request
17 -- Arnold: Dropoff Dan
17 -- Arnold: Request a rider
{'driver_total_distance': 14.0, 'rider_wait_time': 11.0, 'driver_ride_distance': 10.0}
```

## Large Example
```
Events file: events2.txt
0 -- stupid3: Request a rider
0 -- Amaranth: Request a rider
0 -- Almo2nd: Request a driver
0 -- stu5pid3: Request a rider
1 -- stupid4: Request a rider
1 -- Bergamot: Request a rider
1 -- stu6pid4: Request a rider
1 -- stu42pid1: Request a rider
1 -- Almo2222nd: Request a driver
1 -- Amaranth: Pickup Almo2nd
2 -- Crocus: Request a rider
2 -- stupid5: Request a rider
3 -- Dahlia: Request a rider
3 -- Dahlia6: Request a rider
3 -- Ceri777se: Request a driver
3 -- Amaranth: Dropoff Almo2nd
3 -- stu6pid4: Pickup Ceri777se
3 -- Amaranth: Request a rider
4 -- stupid1: Request a rider
4 -- Edelweis5s: Request a rider
4 -- Dahlia6: Request a rider
4 -- Bisq222ue: Request a driver
4 -- stu5pid3: Pickup Almo2222nd
5 -- Bisq3ue: Request a driver
5 -- stupid2: Request a rider
5 -- Foxglov4e: Request a rider
5 -- Bisq2ue: Request a driver
5 -- Bi1sq3ue: Request a driver
5 -- st2upid2: Request a rider
5 -- Dahl123ia: Request a rider
5 -- Crocus: Pickup Bisq3ue
6 -- stu6pid4: Dropoff Ceri777se
6 -- stupid1: Pickup Bi1sq3ue
6 -- stu6pid4: Request a rider
7 -- Amara2nth: Request a rider
7 -- stu42pid1: Pickup Bisq222ue
7 -- Crocus: Dropoff Bisq3ue
7 -- Crocus: Request a rider
8 -- Ber23gamot: Request a rider
8 -- Edelweis5s: Request a rider
8 -- stupid1: Dropoff Bi1sq3ue
8 -- stupid1: Request a rider
9 -- Croc12us: Request a rider
9 -- Bisq222ue: Cancel request
9 -- stupid5: Pickup Bisq2ue
10 -- Ceri7se: Request a driver
10 -- Almo2nd: Cancel request
10 -- stu5pid3: Dropoff Almo2222nd
10 -- Bisq3ue: Cancel request
10 -- Bisq2ue: Cancel request
10 -- Bi1sq3ue: Cancel request
10 -- Foxglov4e: Pickup Ceri7se
10 -- stu5pid3: Request a rider
11 -- stu6pid5: Request a rider
11 -- Almo2222nd: Cancel request
12 -- stu42pid1: Dropoff Bisq222ue
12 -- stu42pid1: Request a rider
14 -- stupid5: Dropoff Bisq2ue
14 -- stupid5: Request a rider
15 -- Des4ert: Request a driver
15 -- Dese5rt: Request a driver
15 -- De1s4ert: Request a driver
15 -- Foxglov4e: Request a rider
16 -- Foxglov4e: Dropoff Ceri7se
16 -- Amaranth: Pickup Des4ert
16 -- Foxglov4e: Request a rider
17 -- Des5e5rt: Request a driver
17 -- Amaranth: Dropoff Des4ert
17 -- stu6pid4: Pickup Des5e5rt
17 -- Amaranth: Request a rider
18 -- Ceri777se: Cancel request
18 -- Crocus: Pickup Dese5rt
18 -- stupid2: Pickup De1s4ert
19 -- Crocus: Dropoff Dese5rt
19 -- Crocus: Request a rider
20 -- Eggsh3ell: Request a driver
20 -- Cer3ise: Request a driver
20 -- Eg1gsh3ell: Request a driver
20 -- Ce2r3ise: Request a driver
20 -- Des4ert: Cancel request
20 -- Dese5rt: Cancel request
20 -- De1s4ert: Cancel request
21 -- stu6pid4: Dropoff Des5e5rt
21 -- stupid2: Dropoff De1s4ert
21 -- Eggsh3ell: Cancel request
21 -- Dahlia6: Pickup Cer3ise
21 -- Eg1gsh3ell: Cancel request
21 -- Dahlia6: Pickup Ce2r3ise
21 -- stu6pid4: Request a rider
21 -- stupid2: Request a rider
22 -- Des5e5rt: Cancel request
22 -- Crocus: Pickup Eggsh3ell
22 -- st2upid2: Pickup Eg1gsh3ell
22 -- Crocus: Request a rider
22 -- st2upid2: Request a rider
24 -- Dahlia6: Dropoff Cer3ise
24 -- Dahlia6: Dropoff Ce2r3ise
24 -- Dahlia6: Request a rider
24 -- Dahlia6: Request a rider
25 -- Fall2ow: Request a driver
25 -- Fal6low: Request a driver
25 -- Fa2ll2ow: Request a driver
25 -- Fa4l6low: Request a driver
25 -- Ceri7se: Cancel request
25 -- Amara2nth: Pickup Fal6low
25 -- Amara2nth: Dropoff Fal6low
25 -- Amara2nth: Request a rider
26 -- stupid3: Pickup Fall2ow
26 -- stupid4: Pickup Fa2ll2ow
26 -- Croc12us: Pickup Fa4l6low
26 -- Croc12us: Dropoff Fa4l6low
26 -- Croc12us: Request a rider
33 -- stupid3: Dropoff Fall2ow
33 -- stupid4: Dropoff Fa2ll2ow
33 -- stupid3: Request a rider
33 -- stupid4: Request a rider
35 -- Cer3ise: Cancel request
35 -- Ce2r3ise: Cancel request
35 -- Fall2ow: Cancel request
35 -- Fal6low: Cancel request
35 -- Fa2ll2ow: Cancel request
35 -- Fa4l6low: Cancel request
60 -- Egg5shell: Request a driver
60 -- Eg3g5shell: Request a driver
61 -- Egg5shell: Cancel request
61 -- Eg3g5shell: Cancel request
63 -- stu5pid3: Pickup Egg5shell
63 -- stu5pid3: Request a rider
64 -- stu6pid5: Pickup Eg3g5shell
64 -- stu6pid5: Request a rider
{'driver_ride_distance': 2.857142857142857, 'driver_total_distance': 4.666666666666667, 'rider_wait_time': 1.2727272727272727}
```

## Authors

| Name             | GitHub                                     | Email
| ---------------- | ------------------------------------------ | -------------------------
| Chenjie Ni       | [jellycsc](https://github.com/jellycsc)    | nichenjie2013@gmail.com

## Thoughts and future improvements

* The distance in the simulation is estimated by [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry), which may be good enough for simple simulation like this. Distance estimation can be improved using real world data followed by path planning algorithm.

## Contributing to this project

1. Fork it ( https://github.com/jellycsc/Uber-ride-sharing-simulation/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to your feature branch (`git push origin my-new-feature`)
5. Create a new Pull Request

Details are described [here](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project).

## Bug Reporting
Please log bugs under [Issues](https://github.com/jellycsc/Uber-ride-sharing-simulation/issues) tab on Github.  
OR you can shoot an email to <nichenjie2013@gmail.com>
