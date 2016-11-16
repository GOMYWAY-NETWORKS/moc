# moc
MOC (music on console) is a console audio player for LINUX/UNIX designed to be powerful and easy to use.

Main website is https://moc.daper.net/, this software is created and maintained by its authors who can be contacted by [this support page] (https://moc.daper.net/node/269)

Here I spread the specification files (moc.spec) which can be used to build RPMs binary packages of MOC, according to the [Fedora Packaging Guidelines] (http://fedoraproject.org/wiki/Packaging:Guidelines).

This repository will remain activated until new RPM Fusion infrastructure is completed.

#### License
*moc.spec* is under the terms of the MIT license.

*MOC* software is under the terms of *GPLv2+ and GPLv3+* license.

### How to build the RPMs

* Install RPMFusion repositories and tools/libraries for building:

```$ su -c 'dnf install http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm'```
<br/>
```$ su -c 'dnf install rpm-build rpmdevtools'```

* Create directories for RPM building under your home

`$ rpmdev-setuptree`

You will see something like that:

`$ ls $HOME/rpmbuild`<br/>
`BUILD  BUILDROOT  RPMS  SOURCES  SPECS  SRPMS`

* Download [*moc* src-rpm](https://github.com/sagitter/moc/releases) and push it in `$HOME/rpmbuild/SRPMS` directory

* Install *moc* related dependencies for building

`$ cd $HOME/rpmbuild/SRPMS`<br/>
`$ su -c 'dnf builddep libav?-src.rpm'`

* Build 'moc' binary RPMs

`$ cd $HOME/rpmbuild/SRPMS`<br/>
`$ rpmbuild -bb moc-?-src.rpm`

RPMs building time depends by performance of your system; so, be patient.

* Install *moc*

*rpmbuild* tool will build three RPM packages in $HOME/rpmbuild/RPMS/x86_64(or i386)

`$ cd $HOME/rpmbuild/RPMS/x86_64(or i386)`<br/>
`$ su -c 'dnf install moc-?.arch.rpm'`

#### Packager: 
[sagitter] (https://fedoraproject.org/wiki/User:Sagitter)

#### Contact:  
sagitter AT fedoraproject DOT org
