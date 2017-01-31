# Lucid Cookiecutter for Flask

To use this project, you'll need to install `cookiecutter`. Feel free to
install it globally or within a virtualenv.

    virtualenv env
    . env/bin/activate
    pip install cookiecutter

Then, run cookiecutter and give a target for where you'd like to create your new
project. I have all my work in my $HOME/src dir. Cookiecutter will prompt you to
fill in a new `app_name`. This template expects you to pick a simple name that
only uses underscores for spaces. For example, `mardi_gras` or `carnaval`. The
`app_name` will be what you should use as the github repo name, so the
respective github repos for the aforementioned new projects would be
`lucidhq/mardi_gras` or `lucidhq/carnaval`. Python is a little finicky about
dashes.

    cookiecutter -o $HOME/src git@github.com:lucidhq/cookiecutter-flask.git

## Development on the Cookiecutter itself

If you want to improve the template, feel free to submit a PR. You can run
tests on the template itself by running these commands from this cloned
cookiecutter-flask repo on your local machine:

    make bootstrap
    make test

Note that you will need to have a docker-machine running on your machine, such
that commands like `docker images` work without failing to connect to the
daemon, etc...

Good luck, and please raise any issues you see!
