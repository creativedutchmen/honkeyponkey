# Hackaton EET

## Getting started (building your virtual environment)
In the file `environment.yml` you'll find the most common dependencies.
If there are dependencies you think you'll need which are not on the list, don't worry, it is very easy to add them later on.
To create a new environment from the file, run the following command from your DSVM terminal (which you got from ssh or putty):

    conda env create -f environment.yml

You can now create notebooks in the `notebooks` directory from this environment, which is named after your project.
However, your project code (in the `hackaton_eet` directory is not yet available. The nicest way to install this package is by using pip (I could not get it to work in the `environment.yml` file:

    source activate hackaton_eet
    pip install -e .

This will install an editable version of your code in your virtual environment. You can now edit your code without having to reinstall the package every time, and you don't need to mess with your path.
