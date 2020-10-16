#!usr/bin/bash
FILE="../anaconda/bin"
if [ -d "$FILE" ]; then
   echo "Anaconda Exists"
else 
   echo "Getting Anaconda Install Files"
   wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O ~/anaconda.sh
   
   echo "Change script to an executable"
   chmod +x ~/anaconda.sh 

   echo "Installing Anaconda"
   ~/anaconda.sh -b -p $HOME/anaconda
   
   echo "Removing Anaconda Install File"
   rm ~/anaconda.sh
   
   echo "Activating Anaconda"
   source ~/anaconda/bin/activate
   
   echo "Initialize conda"
   conda init
   
   echo "Updating Conda"
   conda update --all
   
   echo "Creating new environment"
   conda env create -f forecast.yml

   echo "Activating environment"
   conda activate forecast
fi
