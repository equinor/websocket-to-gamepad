from setuptools import find_packages, setup

setup(
    name="websocket-to-gamepad",
    description="Code to map websocket input to virtual gamepad (USB HID-device)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Equinor ASA",
    author_email="fg_robots_dev@equinor.com",
    url="https://github.com/equinor/websocket-to-gamepad",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries",
    ],
    include_package_data=True,
    install_requires=[
        "numpy",
        "websocket-client",
        "vgamepad",
        "inputs",
        "websocket-server",
    ],
    extras_require={
        "dev": [
            "black",
            "mypy",
        ]
    },
    python_requires=">=3.8",
)
