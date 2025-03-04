<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Transporter Robots Exercise (Python)</h3>

  <p align="center">
    AMAS Exercise using the AMAK-Python framework
    <br />
    <a href="https://github.com/alexandreprl/amak-python"><strong>AMAK-Python Framework »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alexandreprl/amak-python-exercise-transporter-robots/issues">Report Bug</a>
    ·
    <a href="https://github.com/alexandreprl/amak-python-exercise-transporter-robots/issues">Request Feature</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Exercise

A room contains two area: the pick-up area in green and the drop-off area in red. Multiple boxes are present in the green area and must be moved to the red area.

To do that, a set of autonomous robots have been deployed. These robots can carry one box at a time and drop it anywhere.

The two areas are separated by a wall. To go from one side of the wall to the other, the robots can use two corridors: one at the top one at the bottom. The width of the corridor is such that only one robot can go through it. Also, two robots cannot be at the same location at the same time.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Click on "Use this template" then "Create a new repository"
* Clone your new repository
* Create a virtual environment `python -m venv .venv` (Optional)
* Activate the virtual environment `source .venv/bin/activate` (Optional)
* Install dependencies `pip install -r requirements.txt`
* Run the simulation `python transporter-robots.py`

### Exercise

The class __RobotAgent__ contains the behavior of a transporter robot. A basic version has been implemented in which they randomly move, pick a box if there is one and drop it if they are in the drop zone. Implement a cooperative behavior in which the robots coordinate to move the boxes to the drop zone as fast as possible.

- Launch the project and observe the behavior of the robots
- Implement a cooperative behavior using communication between close robots
- Implement a cooperative behavior using stigmergy (communication through the environment)

Note: The implemented behaviors should work on room 1 and 2. The extra corridor in room 2 should be used to improve the performance of the system. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the LGPL License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




