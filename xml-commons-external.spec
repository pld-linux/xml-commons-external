# TODO: something with org.apache.env.which (currently xml-commons-which.jar in xml-commons),
# then obsolete xml-commons here
Summary:	Apache XML Commons External classes
Summary(pl):	Klasy Apache XML Commons External
Name:		xml-commons-external
Version:	1.3.04
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/xml/commons/%{name}-%{version}-src.tar.gz
# Source0-md5:	5536f87a816c766f4999ed60593a8701
# from http://svn.apache.org/repos/asf/xml/commons/trunk/java/external/build.xml
Source1:	%{name}-build.xml
URL:		http://xml.apache.org/commons/
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache XML Commons External classes:
 - DOM Level 3 from w3c.org
 - SAX 2.0 from megginson.com

%description -l pl
Klasy Apache XML Commons External:
 - DOM Level 3 z w3c.org
 - SAX 2.0 z megginson.com

%package javadoc
Summary:	javadoc documentation for Apache XML Commons External
Summary(pl):	Dokumentacja javadoc dla pakietu Apache XML Commons External
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
javadoc documentation for Apache XML Commons External.

%description javadoc -l pl
Dokumentacja javadoc dla pakietu Apache XML Commons External.

%prep
%setup -q -c

cp %{SOURCE1} build.xml

# for build.xml
mkdir src xdocs
ln -s ../javax ../org ../manifest.commons src

%build
export JAVA_HOME="%{java_home}"
# default 64m is too low
#export ANT_OPTS="-Xmx128m"
%ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/xml-apis.jar $RPM_BUILD_ROOT%{_javadir}/xml-apis-%{version}.jar
install build/xml-apis-ext.jar $RPM_BUILD_ROOT%{_javadir}/xml-apis-ext-%{version}.jar
ln -sf xml-apis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xml-apis.jar
ln -sf xml-apis-ext-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xml-apis-ext.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
	rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc LICENSE* NOTICE README.*
%{_javadir}/xml-apis*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
