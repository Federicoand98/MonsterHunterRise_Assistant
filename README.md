# MonsterHunter Rise Assistant

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![GitHub followers][github-shield]][github-url]

<!-- PROJECT LOGO -->
<p align="center">
	<!--<img src="https://github.com/Federicoand98/AR-Dice/blob/ardice-main/imgs/LoadLogo.png" alt="logo" height="500" width="400"-->
</p>   
  
<br />
<p align="center">
  	<a href="https://github.com/Federicoand98/MonsterHunterRise_Assistant">
  	</a>
  	<h1 align="center">MonsterHunter Rise Assistant</h1>
  	<p align="center">
		Description here
    	<br /> 
		<a href="https://discord.com/api/oauth2/authorize?client_id=943181210987933786&permissions=534723950656&scope=bot%20applications.commands">
			Click here to add this Bot to your guild
		</a>
		<br />
		<br />
    	·
    	<a href="https://github.com/Federicoand98/MonsterHunterRise_Assistant/issues">Report Bug</a>
    	·
    	<a href="https://github.com/Federicoand98/MonsterHunterRise_Assistant/issues">Request Feature</a>
  	</p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
	<summary>
		<h2 style="display: inline-block">Table of Contents</h2>
	</summary>
  	<ol>
    	<li>
      		<a href="#about-the-project">About The Project</a>
      		<ul>
        		<li><a href="#built-with">Built With</a></li>
      		</ul>
    	</li>
    	<li>
      		<a href="#getting-started">Getting Started</a>
      		<ul>
        		<li><a href="#prerequisites">Prerequisites</a></li>
        		<li><a href="#installation">Installation</a></li>
      		</ul>
    	</li>
    	<li><a href="#usage">Usage</a></li>
    	<li><a href="#roadmap">Roadmap</a></li>
    	<li><a href="#contributing">Contributing</a></li>
    	<li><a href="#license">License</a></li>
    	<li><a href="#contact">Contact</a></li>
  	</ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project


### Built With

-   [Visual Studio Code](https://code.visualstudio.com/download)
-   [NodeJS](https://nodejs.org/en/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

-   Git
-   Visual Studio
-   NodeJS

### Installation

1. Install Git at [Download Git](https://git-scm.com/download).
2. Clone the repo.
    ```sh
    git clone https://github.com/Federicoand98/MonsterHunterRise_Assistant
    ```
3. Install the latest version of NodeJS.
4. Open the directory with Visual Studio.
5. Unzip the 7z file in the Resources folder.

<!-- USAGE EXAMPLES -->

## Usage

To use the application:

-   Move to the project folder
	```sh
	cd MonsterHunterRise_Assistant
-	Create your configuration file for the Bot
	```sh
	touch config.json
	```
	This config file is necessary for the bot's token, inside the file paste
	```sh
	{
    	"clientId" : "paste here your bot client id",
    	"guildId" : "paste here your guild id",
    	"token" : "paste here your token"
	}
	```
-	Install the following packages with **npm** package manager
	```sh
	npm install discord.js
	npm install @discordjs/builders @discordjs/rest discord-api-types
	```
-	Deploy the slash commands with
	```sh
	node src/deploy-commands.js
	```
-   Run with:
	```sh
	node src/index.js
	```

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/Federicoand98/MonsterHunterRise_Assistant/issues) for a list of proposed features (and known issues).

### Future developments

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/Federicoand98/MonsterHunterRise_Assistant/blob/main/LICENSE) for more information.

<!-- CONTACT -->

## Contact

Federico Andrucci - federico.andrucci@gmail.com <br>

Project Link: [https://github.com/Federicoand98/MonsterHunterRise_Assistant](https://github.com/Federicoand98/MonsterHunterRise_Assistant)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Federicoand98/MonsterHunterRise_Assistant.svg?style=for-the-badge
[contributors-url]: https://github.com/Federicoand98/MonsterHunterRise_Assistant/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Federicoand98/MonsterHunterRise_Assistant.svg?style=for-the-badge
[forks-url]: https://github.com/Federicoand98/MonsterHunterRise_Assistant/network/members
[stars-shield]: https://img.shields.io/github/stars/Federicoand98/MonsterHunterRise_Assistant.svg?style=for-the-badge
[stars-url]: https://github.com/Federicoand98/MonsterHunterRise_Assistant/stargazers
[issues-shield]: https://img.shields.io/github/issues/Federicoand98/MonsterHunterRise_Assistant.svg?style=for-the-badge
[issues-url]: https://github.com/Federicoand98/MonsterHunterRise_Assistant/issues
[license-shield]: https://img.shields.io/github/license/Federicoand98/MonsterHunterRise_Assistant.svg?style=for-the-badge
[license-url]: https://github.com/Federicoand98/MonsterHunterRise_Assistant/blob/master/LICENSE
[github-shield]: https://img.shields.io/github/followers/Federicoand98.svg?style=social&label=Follow
[github-url]: https://github.com/Federicoand98
