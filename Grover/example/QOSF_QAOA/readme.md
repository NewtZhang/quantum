# Grove for weighted maxcut

The main code for observations can be found in qaoa.ipynb.

Changes to grove are made in the maxcut_qaoa.py graph under pyqaoa to support weighted graphs.

Libraries requires: pyquil and networkx(You will also need qvm from Rigetti's Forest SDK)
Use this:

```
pip3 install -r requirements.txt
```

or

```
conda install --yes --file requirements.txt
```
I am also using a clone and edited version of Grove(to make the maxcut algorithm work for weighted graph) so use the commands below to install that.

```
cd grove
pip install -e .
```


Feel free to use the code :)
