Project Name: Django_Capstone

The Poll app is an app designed to tally up votes.

Table of Contents:

Installation & Usage
Author


Installation & Usuage:

    Docker (locally):
        run the following command in CMD:
        docker run -ti -p 80:8000 richardfriedrichsen/poll_app

        Open chrome and go to the ip: 127.0.0.1
        Since we specified that the port 8000 in docker should be mapped to port 80 locally, we do need to specify a port at the end of the IP.

    Docker (labs.play-with-docker.com):
        run the following command in the terminal:

        docker run -ti -p 80:8000 richardfriedrichsen/poll_app

        Once it's running the port 80 should pop up to be opened. If this is not the case click on "Open Port" enter 80 and click ok.

Author:
Richard Friedrichsen
    
