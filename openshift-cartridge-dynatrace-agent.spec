%global cartridgedir %{_libexecdir}/openshift/cartridges/dynatrace-agent-6
Name:		openshift-cartridge-dynatrace-agent
Version:	0.0.2
Release:	1%{?dist}
Summary:	Dynatrace Monitoring for Java applications deployed on OpenShift JBoss cartridges
Group:		Applications/Internet
License:	ASL 2.0
URL:		http://www.dynatrace.com
Source0:	https://github.com/akirasoft/openshift-cartridge-dynatrace-agent/archive/master.zip
Requires:       rubygem(openshift-origin-node)
Requires:       openshift-origin-node-util
BuildArch: noarch

%description
Dynatrace Monitoring for Java applications deployed on OpenShift JBoss cartridges

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{cartridgedir}
cp -r * %{buildroot}%{cartridgedir}/

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}/env
%{cartridgedir}/metadata
%{cartridgedir}/versions
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/LICENSE

%changelog
* Wed Dec 31 2014 akirasoft <akirasoft@hotmail.com> 0.0.2-1
- new package built with tito

* Wed Dec 31 2014 Michael Villiger <michael.villiger@dynatrace.com> 0.0.1
- Initial creation
