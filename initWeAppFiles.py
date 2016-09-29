import os
import json


root = os.path.dirname(__file__)

configs = json.load(open(os.path.join(root, 'config.json')))

applicationPath = os.path.join(configs['workspace'], configs['applicationName'])
if not os.path.exists(applicationPath):
    raise Exception('app path not found')

print '++ init weapp files for {0} in {1}'.format(configs['applicationName'], applicationPath)

# construct /pages and the files in it
if not os.path.exists(os.path.join(applicationPath, 'pages')):
    os.mkdir(os.path.join(applicationPath, 'pages'))
for page in configs['initFiles']:
    dirs = page.split('/')[:-1]
    fileNamePre = page.split('/')[-1]
    needMakePathTemp = os.path.join(applicationPath, 'pages')
    # print dirs,fileNamePre
    # make pages dirs
    for d in dirs:
        needMakePath = os.path.join(needMakePathTemp, d)
        needMakePathTemp = needMakePath
        if not os.path.exists(needMakePath):
            os.mkdir(needMakePath)

    # make pages files
    filesExtList = ['.js', '.wxml', 'wxss']
    for ext in filesExtList:
        filePath = os.path.join(needMakePath, fileNamePre + ext)
        if not os.path.exists(filePath):
            with open(os.path.join(root, 'temp', 'pageJs{0}.temp'.format(ext)), 'a+') as fp:
                pageContent = fp.read()
            with open(filePath, 'w') as fp:
                fp.write(pageContent)

# write application/app.json
appJsonContent = '", "'.join(configs['initFiles'])
appJsonContent = '"{0}"'.format(appJsonContent)
with open(os.path.join(root, "temp", 'app.json.temp'), 'a+') as fp:
    res = fp.read()
print appJsonContent
# print res.format('hhhh')
appJsonContent = res.replace('{{0}}', appJsonContent)
with open(os.path.join(applicationPath, 'app.json'), 'w') as fp:
    fp.write(appJsonContent)

# write application/app.js
with open(os.path.join(root, "temp", 'app.js.temp'), 'a+') as fp:
    appJsContent = fp.read()
with open(os.path.join(applicationPath, 'app.js'), 'w') as fp:
    fp.write(appJsContent)

# write application/app.wxss
with open(os.path.join(applicationPath, 'app.wxss'), 'w') as fp:
    fp.write("")
