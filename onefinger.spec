# TODO:
# - prepare desktop entry
# - compile python files
Summary:	Graphical interface to the shell
Summary(pl):	Graficzna nak³adka na liniê poleceñ
Name:		onefinger
Version:	3.0
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/onefinger/%{name}-core_%{version}.tar.gz
# Source0-md5:	449da761602e3a8145f8143ea3c262bd
URL:		http://onefinger.sourceforge.net/
Requires:	python-PyKDE
BuildArch:	noarch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Onefinger is a general-purpose GUI (graphical user interface) built on
top of the CLI (command line interface). Although entirely graphical
and "pretty", OneFinger does not attempt to hide the underlying CLI
language: instead, it lets you compose CLI commands with the mouse
(and only one finger!).

%description -l pl
Onefinger jest przeznaczonym do ogólnego u¿ytku GUI (Graficznym
Interfejsem U¿ytkownika) zbudowanym na podstawie linii poleceñ. W
przeciwieñstwie do wiêkszo¶ci graficznych nak³adek, OneFinger nie
próbuje ukrywaæ mo¿liwo¶ci linii poleceñ, przeciwnie, pozwala wybraæ
komendy i prze³±czniki programów korzystaj±c z myszy(tylko jednym
palcem!).

%prep
%setup -q -n %{name}-core_%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}

cp -r src/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
cd %{_datadir}/%{name}/python
python one-finger.py $*
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES TODO doc/* web-site/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
