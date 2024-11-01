#!/bin/bash
# sh test5Sweep.sh 0.0014 0.0024 0.0001 0.50 0.55 0.05

# Create a directory with 'test5sweep' date and time
exp_dir=test5sweep_`date "+%Y-%m-%d_%H.%M.%S"`
mkdir $exp_dir

# Copy py and sh script to the new dir and change dir
cp test5.py $exp_dir
cp test5Sweep.sh $exp_dir
cd $exp_dir

# Assign arguments for (r, a) ranges and steps
low_r=$1
hi_r=$2
step_r=$3
low_a=$4
hi_a=$5
step_a=$6

# Print the parameters being used for the sweep
echo "Parameters are: "
echo
echo "R values : " $low_r $hi_r $step_r
echo "A values : " $low_a $hi_a $step_a
echo
echo
echo "Running simulations..."
echo

# Iterate over r values from low_r to hi_r with step_r increments
for r in `seq $low_r $step_r $hi_r`;
do
# Iterate over a values from low_a to hi_a with step_a increments
    for a in `seq $low_a $step_a $hi_a`;
    do
# Print and simulation with the current r, a values and output to a CSV file
        echo "Experiment: " $r $a
        python test5.py $r $a > "${r}_${a}.csv"
	echo
    done
done
