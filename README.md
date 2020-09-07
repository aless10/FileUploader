# FileUploader
![Run application tests](https://github.com/aless10/FileUploader/workflows/Run%20application%20tests/badge.svg)


A basic file uploader application

## TOC

* [Version](#version)
* [How to run](#how-to-run)

## Version

0.4.0.dev

## How to run it

The application runs inside a docker container. The django application is served via gunicorn with a nginx server in front of it.
The database is a Postgresql that also lives inside another container.

After cloning the repo, you should create a file ``.env`` with the environment variables that you want to use. You can find and example [here]([.env.sample))
Then you can run in the terminal:
    
    ./local/build.sh (it builds the app container)
    ./local/start.sh (it runs the docker-compose command)

This should start the containers with the settings found in the ``.env`` file.
In the ``local`` folder there are some script to run:
    
    ./local/runtests_local.sh to run the tests as localhost
    ./local/runtests_remote.sh to run the tests in docker containers

## Install git client Hooks

1. Open with a terminal and run
```bash
$ git config core.hooksPath git-hooks
```

The command above set git to use hooks saved in `git-hooks` instead of the default `.git/hooks/`.
This installation is required because [git doesn't track git client hooks.](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)

The pre-commit hook performs a check using flake8 with the same settings used during the deployment
The environment needs to be activated in order for the hook to work
