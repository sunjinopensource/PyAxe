import os


class Path:
    def __init__(self, version):
        """
        :param version: vs version number such as 9, 10, 12, 14, 15
        
        注意：从VS15(VS2017)开始，系统不再提供环境变量VS150COMNTOOLS
        https://developercommunity.visualstudio.com/content/problem/25776/vs150comntools-does-not-exists.html
        
        因此若version>=15，需手工建立环境变量，如：VS150COMNTOOLS=D:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\Common7\Tools
        """
        self.Version = version
        
        if os.name == 'nt':
            self.CommonTools = os.environ['VS%d0COMNTOOLS' % version]
        else:
            self.CommonTools = ''

        self.Root = os.path.normpath(os.path.join(self.CommonTools, '..', '..'))

        self.IDE = os.path.normpath(os.path.join(self.CommonTools, '..', 'IDE'))        
        self.DevenvEXE = os.path.join(self.IDE, 'devenv.exe')
        
        self.VC = os.path.join(self.Root, 'VC')

        MSBuildRoot = r'C:\Program Files (x86)'
        if version >= 15:
            MSBuildRoot = self.Root
        self.MSBuildEXE = r'"%s\MSBuild\%d.0\Bin\MSBuild.exe"' % (MSBuildRoot, version)
            