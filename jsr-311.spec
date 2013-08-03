Name: jsr-311
Version: 1.1.1
Release: 5%{?dist}
Summary: JAX-RS: Java API for RESTful Web Services
Group: Development/Libraries
License: CDDL
Url: http://jsr311.java.net

# svn export https://svn.java.net/svn/jsr311~svn/tags/jsr311-api-1.1.1 jsr-311-1.1.1
# tar cvzf jsr-311-1.1.1.tgz jsr-311-1.1.1
Source0: %{name}-%{version}.tgz

# Patch the POM:
Patch0: %{name}-pom.patch

BuildRequires: java-devel
BuildRequires: jpackage-utils

BuildRequires: buildnumber-maven-plugin
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

Requires: jpackage-utils
Requires: java

BuildArch: noarch


%description
JAX-RS: Java API for RESTful Web Services


%package javadoc
Summary: Javadocs for %{name}
Group: Documentation
Requires: jpackage-utils


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0


%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install \
  javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jsr311-api-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_javadir}/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2011 Juan Hernandez <juan.hernandez@redhat.com> 1.1.1-1
- Adapted (mostly copied, in fact) from the corresponding package from Mageia
  (http://www.mageia.org) with support from Gil Cattaneo <puntogil@libero.it>.

