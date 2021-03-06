"""
Definition of urls for DjangoSalicornia.
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import login
from rest_framework_swagger.views import get_swagger_view

from saliapp import views
from saliapp.views import *

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), 'home')

schema_view = get_swagger_view(title='API documentation')

urlpatterns = [

    # url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/$', login_required(schema_view), name="api-doc"),

    url(r'^$', login_forbidden(login), name="login"),
    url(r'^home/$', home, name='home'),

    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout_page),

    url(r'^manageruser/$', login_required(ManagerUserCompany.as_view()), name='managerUser'),


    url(r'^validateuser/(?P<id_user>[-\w]+)/$', views.validate_user, name='validateuser'),
    url(r'^removeuser/(?P<id_user>[-\w]+)/(?P<to_redirect>[-\w]+)/$', views.remove_user, name='removeuser'),

    url(r'^managercompany/$', login_required(ManagerCompany.as_view()), name='managercompany'),

    url(r'^manageruserall/$', login_required(ManagerAllUser.as_view()), name='manageruserall'),

    url(r'^profile/$', views.profile, name='profile'),

    url(r'^admin/', admin.site.urls),

    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^recover/$', views.recover, name='recover'),

    # url(r'^recoverpassword/', views.recoverpassword),

    # Add coisas

    url(r'^devices/cm/all/$', login_required(ShowDevices.as_view()), name="addcpu"),
    url(r'^addsensor/$', views.add_sensor, name="addsensor"),
    url(r'^addmodule/$', views.add_module, name="addmodule"),

    url(r'^deletecm/(?P<id_cpu>[-\w]+)/$', views.deletecm, name="deletecm"),

    url(r'^devices/cm/(?P<id_cm>[-\w]+)/$', login_required(ShowSensorModule.as_view()), name="showdetails"),

    url(r'^addsm/(?P<id_cm>[-\w]+)/$', views.addSensorModule, name="addsm"),

    url(r'^devices/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)/visual/(?P<dates>[-\w]+)/(?P<datef>[-\w]+)$',
        login_required(SensorValues.as_view()),
        name="viewSensors"),

    url(r'^typesensor/$', login_required(TypeSensor.as_view()), name="typesensor"),

    url(r'^typecommunication/$', login_required(TypeCommunication.as_view()), name="typecommunication"),

    url(r'^deletecomm/(?P<id_comm>[-\w]+)/$', views.deletecomm, name="deletecomm"),

    url(r'^deletesm/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)$', views.deletesm, name="deletesm"),

    url(r'^deletesensor/(?P<id_sensor>[-\w]+)/$', views.deletesensor, name="deletesensor"),

    url(r'^deleteallarm/(?P<id_allarm>[-\w]+)/$', views.checkedAllarms, name="deleteallarm"),

    url(r'^devices/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)/dataset/(?P<dates>[-\w]+)/(?P<datef>[-\w]+)$',
        views.showalldata, name="showalldata"),

    url(r'^devices/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)/export/$', views.exportcsv, name="exportcsv"),

    # url(r'^post1/$', views.post1, name="post1"),


    # API

    #    url(r'^sensor/', views.SensorViewSet.as_view()),
    #    url(r'^medicoes/', views.MeasureViewSet.as_view()),
    #    url(r'^tudo/', views.SensorMeasurementsViewSet.as_view()),



    # communication type
    url(r'^api/communication/$', views.CommunicationTypeList.as_view()),
    url(r'^api/communication/(?P<pk_or_name>[-\w]+)/$', views.CommunicationType_param.as_view(), name='comm_type'),

    # sensor type
    url(r'^api/sensortype/$', views.SensorTypeList.as_view()),
    url(r'^api/sensortype/(?P<pk_or_name>[-\w]+)/$', views.SensorType_param.as_view()),

    # user
    url(r'^api/user/$', views.UserList.as_view(), name='user'),
    url(r'^api/user/(?P<pk_or_username>[-\w]+)/$', views.User_param.as_view(), ),

    # cm
    url(r'^api/cm/$', views.ControllerModuleList.as_view()),
    url(r'^api/cm/(?P<pk_or_name>[-\w]+)/$', views.ControllerModule_param.as_view()),

    # cm per users

    url(r'^api/cmperusers/(?P<pk_or_username>[-\w]+)/$', views.CMperUser_param.as_view()),

    # sm
    url(r'^api/sm/$', views.SensorModuleList.as_view()),
    url(r'^api/sm/(?P<pk_or_name>[-\w]+)/$', views.SensorModule_param.as_view()),

    # sm per cm
    url(r'^api/smpercm/$', views.SMperCMList.as_view()),
    url(r'^api/smpercm/(?P<pk_or_name_cm>[-\w]+)$', views.SMperCM_param.as_view()),

    # sensor
    url(r'^api/sensor/$', views.SensorList.as_view()),
    url(r'^api/sensor/(?P<pk_or_sensor_type>[-\w]+)$', views.Sensor_param.as_view()),

    # sensor per sm
    url(r'^api/sensorpersm/(?P<id_sm_or_name_sm>[-\w]+)$', views.SensorperSM_param.as_view()),

    # reading
    url(r'^api/reading/(?P<id_sensor>[0-9]+)/(?P<date_start>[-\w]+)/(?P<date_end>[-\w]+)$',
        views.Reading_param.as_view()),
    url(r'^api/reading/(?P<id_sensor>[0-9]+)$',
        views.Reading_param_all.as_view()),

    # allarms settings
    url(r'^api/alarmssettings/(?P<id_sensor>[0-9]+)$', views.AlarmsSettings_param.as_view()),

    # allarms
    url(r'^api/alarms_reading/(?P<id_reading>[0-9]+)$', views.Alarms_param_reading.as_view()),
    url(r'^api/alarms_sensor/(?P<id_sensor>[0-9]+)$', views.Alarms_param_sensor.as_view()),  ### problemaaaa


    url(r'^changestatevalve/(?P<state>[-\w]+)/(?P<id_sensor>[-\w]+)$', views.changestatevalve),


]

# urlpatterns = format_suffix_patterns(urlpatterns)
