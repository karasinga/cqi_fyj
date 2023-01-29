from django.urls import path
from project.views import *

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('deep-dive-facilities/', deep_dive_facilities, name="deep_dive_facilities"),
    # path('login/', login_page, name="login_page"),
    # path('register/', register_page, name="register"),
    # path('update-profile/<int:pk>', update_profile, name="update_profile"),
    path('update-profile/', update_profile, name="update_profile"),
    path('deep-dive-chmt/', deep_dive_chmt, name="deep_dive_chmt"),
    # path('qi-team-members/', qi_team_members, name="qi_team_members"),
    path('qi-team-members/', qi_team_members_view, name="qi_team_members"),
    # path('qi-managers/', qi_managers, name="qi_managers"),
    path('qi-managers/', qi_managers_view, name="qi_managers"),
    path('archived/', archived, name="archived"),
    path('audit-trail/', audit_trail, name="audit_trail"),
    # path('comments/', comments, name="comments"),
    path('show_all_comments/', show_all_comments, name="comments"),
    path('comments-no-response/', comments_no_response, name="comments_no_response"),
    path('comments-with-response/', comments_with_response, name="comments_with_response"),
    path('single-project-comments/<int:pk>/', single_project_comments, name="single_project_comments"),
    path('update-comments/<int:pk>/', update_comments, name="update_comments"),
    path('comments-response/<int:pk>/', comments_response, name="comments_response"),
    path('update-response/<int:pk>/', update_response, name="update_response"),
    path('untracked-projects/', untracked_projects, name="untracked_projects"),
    path('resources/', resources, name="resources"),
    path('sub-counties-list/', sub_counties_list, name="sub_counties_list"),
    path('single-project/<int:pk>', single_project, name="single_project"),
    path('facility-projects/<str:pk>', facility_project, name="facility_project"),
    path('department-projects/<str:pk>', department_project, name="department_project"),
    path('department-all-projects/<str:pk>', department_filter_project, name="department_filter_project"),
    path('qi-managers-own-project/<int:pk>', qi_managers_filter_project, name="qi_managers_filter_project"),
    path('facility-all-projects/<str:pk>', facility_filter_project, name="facility_filter_project"),
    path('qicreator-all-projects/<str:pk>', qicreator_filter_project, name="qicreator_filter_project"),
    path('county-all-projects/<str:pk>', county_filter_project, name="county_filter_project"),
    path('subcounty-all-projects/<str:pk>', sub_county_filter_project, name="sub_county_filter_project"),
    path('qi-creator/<str:pk>', qi_creator, name="qi_creators"),
    path('qi-managers-projects/<int:pk>', qi_managers_projects, name="qi_managers_projects"),
    path('canceled-projects/<str:pk>', canceled_projects, name="canceled_projects"),
    path('not-started/<str:pk>', not_started, name="not_started"),
    path('completed-closed/<str:pk>', completed_closed, name="completed_closed"),
    path('add-lesson-learnt/<int:pk>', add_lesson_learnt, name="add_lesson_learnt"),
    path('lesson-learnt/', lesson_learnt, name="lesson_learnt"),
    path('show-qi-project-comments/<int:pk>', show_project_comments, name="show_project_comments"),
    path('like-dislike/<int:pk>', like_dislike, name="like_dislike"),


    # path('archive-project/<int:project_id>', archive_project, name="archive_project"),
    # path('unarchive-project/<int:pk>', unarchive_project, name="unarchive_project"),
    path('unarchive-project/<int:project_id>', toggle_archive_project, name="toggle_archive_project"),
    path('ongoing-projects/<str:pk>', ongoing, name="ongoing"),
    path('measurement-frequency/<str:pk>', measurement_frequency, name="measurement_frequency"),
    path('postponed/<str:pk>', postponed, name="postponed"),
    path('add-stake-holders/<int:pk>', add_stake_holders, name="add_stake_holders"),
    path('add-qi-manager/', add_qi_manager, name="add_qi_manager"),
    path('add-department/', add_department, name="add_department"),
    path('add-category/', add_category, name="add_category"),
    path('add-subcounty/', add_subcounty, name="add_subcounty"),
    path('add-facility/', add_facility, name="add_facility"),
    path('add-county/', add_county, name="add_county"),
    path('add-resources/', add_resources, name="add_resources"),
    path('add-project/', add_project, name="add_project"),
    path('choose-project-level/', choose_project_level, name="choose_project_level"),
    path('add-project/facility', add_project_facility, name="add_project_facility"),
    path('add-project/subcounty', add_project_subcounty, name="add_project_subcounty"),
    path('add-project/county', add_project_county, name="add_project_county"),
    path('add-project/hub', add_project_hub, name="add_project_hub"),
    path('add-project/program', add_project_program, name="add_project_program"),
    path('add-qi-team-member/<int:pk>', add_qi_team_member, name="add_qi_team_member"),
    path('add-project-milestone/<int:pk>', add_project_milestone, name="add_project_milestone"),
    path('add-corrective-action/<int:pk>', add_corrective_action, name="add_corrective_action"),
    path('add-lesson-learnt/', add_lesson_learnt, name="add_lesson_learnt"),
    path('add-baseline-image/<int:pk>', add_baseline_image, name="add_baseline_image"),
    path('create-comment/<int:pk>', create_comment, name="create_comment"),

    path('qi-projects-involved-in/<int:pk>', qi_team_involved, name="qi_team_involved"),

    path('facilities-landing-page/', facilities_landing_page, name="facilities_landing_page"),
    path('update-project/<int:pk>/', update_project, name="update_project"),
    path('tested-change/<int:pk>/', tested_change, name="tested_change"),
    path('update-test-of-change/<int:pk>/', update_test_of_change, name="update_test_of_change"),
    path('update-resource/<int:pk>/', update_resource, name="update_resource"),
    path('update-qi-managers/<int:pk>/', update_qi_managers, name="update_qi_managers"),
    path('update-qi-team-member/<int:pk>/', update_qi_team_member, name="update_qi_team_member"),
    path('update-milestone/<int:pk>/', update_milestone, name="update_milestone"),
    path('update-sub-counties/<int:pk>/', update_sub_counties, name="update_sub_counties"),
    path('update-action-plan/<int:pk>/', update_action_plan, name="update_action_plan"),
    path('update-lesson-learnt/<int:pk>/', update_lesson_learnt, name="update_lesson_learnt"),
    path('update-baseline/<int:pk>/', update_baseline, name="update_baseline"),
    path('update-fields', update_fields, name="update_fields"),

    path('update-comments/<int:pk>/', update_comments, name="update_comments"),

    path('delete-test-of-change/<int:pk>/', delete_test_of_change, name="delete_test_of_change"),
    path('delete-project/<int:pk>', delete_project, name="delete_project"),
    path('delete-commment/<int:pk>/', delete_comment, name="delete_comment"),
    path('delete-response/<int:pk>/', delete_response, name="delete_response"),
    path('delete-resource/<int:pk>/', delete_resource, name="delete_resource"),
    path('delete-qi-team-member/<int:pk>/', delete_qi_team_member, name="delete_qi_team_member"),
    path('delete-milestone/<int:pk>/', delete_milestone, name="delete_milestone"),
    path('delete-action-plan/<int:pk>/', delete_action_plan, name="delete_action_plan"),
    path('delete-lesson-learnt/<int:pk>/', delete_lesson_learnt, name="delete_lesson_learnt"),
    path('delete-comments/<int:pk>/', delete_comments, name="delete_comments"),
]
