for i in 1 #0.000000001 0.00001 0.00005 0.0001 0.0003 0.0005 0.0007 0.0009 0.001 0.002
do
echo $i
python build_EPSP_net.py $i
python run_save_network.py $i
done
