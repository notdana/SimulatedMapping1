from setuptools import setup
import os
import glob

package_name = 'dev_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "launch"),glob.glob(os.path.join("launch","*.launch.py"))),
        (os.path.join("share", package_name, "description"),glob.glob(os.path.join("description","*.urdf.xacro"))),
        (os.path.join("share", package_name, "description"),glob.glob(os.path.join("description","*.xacro"))),
        (os.path.join("share", package_name, "config"),glob.glob(os.path.join("config","*.yaml"))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='ros@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node_x = dev_pkg.test_node:main",
            "dev_map_x = dev_pkg.dev_map:main",
            "tf_node_x = dev_pkg.tf_node:main",
        ],
    },
)
