<!-- ABOUT THE PROJECT -->
## About The Project
A Complete End to End System from 𝐌𝐨𝐝𝐞𝐥 𝐂𝐮𝐬𝐭𝐨𝐦𝐢𝐳𝐚𝐭𝐢𝐨𝐧 To 𝐄𝐝𝐠𝐞 𝐃𝐞𝐯𝐢𝐜𝐞 𝐃𝐞𝐩𝐥𝐨𝐲𝐦𝐞𝐧𝐭.
I have used a popular 𝐈𝐦𝐚𝐠𝐞 𝐒𝐞𝐠𝐦𝐞𝐧𝐭𝐚𝐭𝐢𝐨𝐧 𝐌𝐨𝐝𝐞𝐥 - 𝐔𝟐-𝐍𝐞𝐭. I have customized the implementation of this model for background removal of image and video and deployed in Django server, created API's for Communication between the Model Server with Intermediate Server(PHP) and Connected to Frontend(React.js) in web and Native Android for mobile.

![Project Workflow (4)](https://github.com/MahendraKumar851744/bg-removal-final/assets/105593585/f01ffeb9-ced5-4022-a963-3c3b39ab2640)

## Getting Started

Background Remover is an online tool to remove background from image and video using AI, made by Mahendra.

### Requirements

Download the model weights from this link: https://drive.google.com/file/d/11OF3zcm71nvmsE0P1vBZK109nHVu3eVr/view?usp=drive_link and save the file in remover/u2net/saved_models

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/MahendraKumar851744/bg-removal-final
   ```
2. Install pip packages
   ```sh
   python >= 3.8
   django
   numpy==1.15.2
   scikit-image==0.14.0
   torch
   torchvision
   pillow==8.1.1
   opencv-python
   paddlepaddle
   paddlehub
   gradio
   ```
## Usage
  ```sh
      cd project
      python manage.py runserver
  ```


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


## Contact
LinkedIn - https://www.linkedin.com/in/mahendra-kumar-b5881324b/
Gmail - androiprogrammers@gmail.com


## Acknowledgments
https://arxiv.org/pdf/2005.09007.pdf
https://github.com/NathanUA/U-2-Net
https://github.com/pymatting/pymatting
https://github.com/danielgatis/rembg
https://github.com/ecsplendid/rembg-greenscreen
https://superuser.com/questions/1647590/have-ffmpeg-merge-a-matte-key-file-over-the-normal-video-file-removing-the-backg
https://superuser.com/questions/1648680/ffmpeg-alphamerge-two-videos-into-a-gif-with-transparent-background/1649339?noredirect=1#comment2522687_1649339
https://superuser.com/questions/1649817/ffmpeg-overlay-a-video-after-alphamerging-two-others/1649856#1649856


## License
Code Licensed under MIT License Models Licensed under Apache License 2.0
