export default {
    "particles": {
      "number": {
        "value": 80, // No of images
        "density": {
          "enable": true,
          "value_area": 600 // Specify area (Lesser is greater density)
        }
      },
      "color": {
        "value": "#5affd4"
      },
      "shape": {
        "type":  [
          'image',
          'image2',
          'image3',
          'image4',
          'image5',
          'image6',
          'image7',
          'image8',
          'image9',
          'image10',
          'image11',
          'image12',
          'image13',
          'image14',
          'image15',
          'image16'
        ],
        "stroke": {
          "width": 0,
        },
        "polygon": {
          "nb_sides": 16
        },
        "image": {
          "src": 'img/logos/git.png'
        }
      },
      "opacity": {
        "value": 0.3, // Adjust opactiy
        "random": false,
        "anim": {
          "enable": false,
          "speed": 1,
          "opacity_min": 0.1,
          "sync": false
        }
      },
      "size": {
        "value": 100, // Adjust the image size
        "random": true,
        "anim": {
          "enable": true,
          "speed": 5,
          "size_min": 20,
          "sync": false
        }
      },
      "line_linked": {
        "enable": false,
        "distance": 500,
        "color": "#ffffff",
        "opacity": .3,
        "width": 10
      },
      "move": {
        "enable": true,
        "speed": 2,   // Speed of particle motion
        "direction": "none",
        "random": false,
        "straight": false,
        "out_mode": "out",
        "bounce": false,
        "attract": {
          "enable": false,
          "rotateX": 600,
          "rotateY": 1200
        }
      }
    },
    "interactivity": {
      "detect_on": "canvas",
      "events": {
        "onhover": {
          "enable": false,
          "mode": "grab"
        },
        "onclick": {
          "enable": false,
          "mode": "push"
        },
        "resize": true
      },
      "modes": {
        "grab": {
          "distance": 400,
          "line_linked": {
            "opacity": 1
          }
        },
        "bubble": {
          "distance": 400,
          "size": 40,
          "duration": 2,
          "opacity": 8,
          "speed": 3
        },
        "repulse": {
          "distance": 200,
          "duration": 0.4
        },
        "push": {
          "particles_nb": 4
        },
        "remove": {
          "particles_nb": 2
        }
      }
    },
    "retina_detect": false
  }
