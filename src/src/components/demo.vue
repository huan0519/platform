<template>
    <div class="part_back" id="app">
        <vue-particles id="tsparticles" :particlesLoaded="particlesLoaded" :options="particlesOptions"></vue-particles>
    </div>

</template>

<script>
    import { VueParticles } from '@tsparticles/vue2';

export default {
  component: {
    VueParticles
  },
  data() {
    return {
      particlesOptions: {

        background:{
            color:"#808080"
        },
        particles: {
          number: {
            value: 150,
          },
          color: {
            value: '#00FF00',
          },
          shape: {
            type: 'circle',
          },
          opacity: {
            value: 0.8,
          },
          size: {
            value: 3,
          },
          animate: {
            enable: true,
            speed: 20,
            direction: 'up',
          },
          interaction: {
            detect_on: 'canvas',
            events: {
              onclick: {
                enable: true,
                mode: 'push',
              },
            },
            modes: {
              push: {
                quantity: 4,
              },
            },
        }
    }
    }
  }    
  },
  mounted() {
    this.$nextTick(() => {
      const particlesInit = (engine) => {
        if (engine.isLoaded()) {
          const options = {
            particles: {
              number: {
                value: 150,
                density: {
                  enable: true,
                  value_area: 800,
                },
              },
              color: {
                value: '#ffffff',
              },
              shape: {
                type: 'circle',
              },
              opacity: {
                value: 0.5,
                random: false,
                anim: {
                  enable: false,
                  speed: 1,
                  opacity_min: 0.1,
                  sync: false,
                },
              },
              size: {
                value: 3,
                random: true,
                anim: {
                  enable: false,
                  speed: 4,
                  size_min: 0.1,
                  sync: false,
                },
              },
              line_linked: {
                enable: true,
                distance: 150,
                color: '#ffffff',
                opacity: 0.4,
                width: 1,
              },
              move: {
                enable: true,
                speed: 1,
                direction: 'none',
                random: false,
                straight: false,
                out_mode: 'out',
                bounce: false,
                attract: {
                  enable: false,
                  rotateX: 600,
                  rotateY: 1200,
                },
              },
            },
            interactivity: {
              detect_on: 'canvas',
              events: {
                onhover: {
                  enable: true,
                  mode: 'repulse',
                },
                onclick: {
                  enable: true,
                  mode: 'push',
                },
                resize: true,
              },
              modes: {
                grab: {
                  distance: 400,
                  line_linked: {
                    opacity: 1,
                  },
                },
                bubble: {
                  distance: 400,
                  size: 40,
                  duration: 2,
                  opacity: 8,
                  speed: 3,
                },
                repulse: {
                  distance: 200,
                  duration: 0.4,
                },
                push: {
                  particles_nb: 4,
                },
                remove: {
                  particles_nb: 2,
                },
              },
            },
            retina_detect: true,
          };
          engine.load(options);
        }
      };
      // Load the particles
      tsParticles.load(particlesInit);
    });
  },
  methods: {
    particlesLoaded(instance) {
      // 粒子加载完成后的回调
    },
  },
};
</script>

<style>
  .part_back{
    position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  }
</style>
