%global cartridgedir %{_libexecdir}/openshift/cartridges/dynatrace-agent-6
Name:		openshift-cartridge-dynatrace-agent
Version:	0.0.7
Release:	1%{?dist}
Summary:	Dynatrace Monitoring for Java applications deployed on OpenShift JBoss cartridges
Group:		Applications/Internet
License:	ASL 2.0
URL:		http://www.dynatrace.com
#Source0:	https://github.com/akirasoft/openshift-cartridge-dynatrace-agent/archive/master.zip
Source0:        %{name}-%{version}.tar.gz
Requires:       rubygem(openshift-origin-node)
Requires:       openshift-origin-node-util
BuildArch:      x86_64
%define _unpackaged_files_terminate_build 0
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Dynatrace Monitoring for Java applications deployed on OpenShift JBoss cartridges

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{cartridgedir}
cp -r * %{buildroot}%{cartridgedir}/

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}/env
%dir %{cartridgedir}/metadata
%{cartridgedir}/versions
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/LICENSE

%changelog
* Tue Apr 21 2015 Mike Villiger <akirasoft@hotmail.com> 0.0.7-1
removed erb file, moved JAVA_OPTS_EXT to start action within control script
- 

* Mon Apr 20 2015 Mike Villiger <akirasoft@hotmail.com> 0.0.6-1
- added env-dir to control script (akirasoft@hotmail.com)

* Wed Jan 07 2015 Mike Villiger <akirasoft@hotmail.com> 0.0.5-1
- specfile change to source0

* Wed Jan 07 2015 Mike Villiger <akirasoft@hotmail.com> 0.0.4-1
- changed spec
- changed tito.props (akirasoft@hotmail.com)
- adding setup back again (akirasoft@hotmail.com)
- Updated spec file to remove comment out setup
  (dynatrace@broker.openshift.local)
- updated tito build props (akirasoft@hotmail.com)
- specfiles are stupid (akirasoft@hotmail.com)

* Wed Dec 31 2014 akirasoft <akirasoft@hotmail.com> 0.0.3-1
- specfile changes (akirasoft@hotmail.com)
- adjusted arch for spec file (akirasoft@hotmail.com)
- still more spec file changes (akirasoft@hotmail.com)
- more spec file changes (akirasoft@hotmail.com)
- updating spec (akirasoft@hotmail.com)
- final spec file (akirasoft@hotmail.com)
* Wed Dec 31 2014 akirasoft <akirasoft@hotmail.com> 0.0.2-1
- new package built with tito

* Wed Dec 31 2014 Michael Villiger <michael.villiger@dynatrace.com> 0.0.1
- Initial creation
