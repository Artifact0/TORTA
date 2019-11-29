#!/bin/sh
echo #
echo #
echo #
while true; do
    python3 torta.py
    read -p "Would you like to rerun Torta?" yn
    case $yn in
        [Yy]* ) continue;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
done

