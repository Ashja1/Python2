from setuptools import setup, find_packages
setup(
    name = "Boids",
    version = "0.1",
    description='Boid Simulation',
    author='Ashja Rabed',
    author_email='ashja.rabed.16@ucl.ac.uk',
    license='MIT',
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/boids'],
    install_requires = ['matplotlib', 'numpy', 'pyyaml', 'argparse']
)
