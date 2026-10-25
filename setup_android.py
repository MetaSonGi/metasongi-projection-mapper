from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parent
P=ROOT/'AndroidProject'
files={
'settings.gradle':"pluginManagement { repositories { google(); mavenCentral(); gradlePluginPortal() } }\ndependencyResolutionManagement { repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS); repositories { google(); mavenCentral() } }\nrootProject.name = 'MetaSonGiMapper'\ninclude ':app'\n",
'build.gradle':"plugins { id 'com.android.application' version '8.9.2' apply false }\n",
'app/build.gradle':"plugins { id 'com.android.application' }\nandroid { namespace 'com.metasongi.mapper'; compileSdk 35; defaultConfig { applicationId 'com.metasongi.mapper'; minSdk 26; targetSdk 35; versionCode 1; versionName '0.1' } }\n",
'gradle.properties':"org.gradle.jvmargs=-Xmx2048m\n",
'app/src/main/AndroidManifest.xml':'''<manifest xmlns:android="http://schemas.android.com/apk/res/android"><application android:label="MetaSonGi Mapper" android:theme="@android:style/Theme.Material.NoActionBar" android:allowBackup="false"><activity android:name=".MainActivity" android:exported="true"><intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter></activity></application></manifest>'''
}
files['app/src/main/java/com/metasongi/mapper/MainActivity.java']=(ROOT/'MainActivity.java').read_text()
for name,text in files.items():
 p=P/name;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists() and p.read_text()!=text:raise SystemExit(f'Refusing to overwrite changed file: {p}')
 p.write_text(text,encoding='utf-8')
print('Open in Android Studio:',P)
print('Use JDK 17 and Gradle 8.11.1. If prompted choose local Gradle 8.11.1; no wrapper JAR is bundled.')
