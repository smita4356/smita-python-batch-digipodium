
def setting_fun(filename='settings',**details):

    if details:
        with open('settings.abcd','w') as file:
            for k,v in details.items():
                file.write(f'{k}-->{v}')
setting_fun(color='blue',alpha=.1,filename='color_setting.txt')
setting_fun(ram=2,windows='95',version=3,filename='pcsetting.txt')