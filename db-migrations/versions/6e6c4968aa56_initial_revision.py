"""Initial revision

Revision ID: 6e6c4968aa56
Revises:
Create Date: 2017-09-19 15:47:32.370609

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6e6c4968aa56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.Text(), nullable=False),
    sa.Column('surname', sa.Text(), nullable=False),
    sa.Column('nickname', sa.Text(), nullable=False),
    sa.Column('public_nickname', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('gender', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('group_uid', sa.Integer(), nullable=True),
    sa.Column('last_action', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('last_login', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('registered', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('token', sa.Text(), nullable=True),
    sa.Column('token_timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['group_uid'], ['groups.uid'], ),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('nickname')
    )
    op.create_table('languages',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('ui_locales', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('ui_locales')
    )
    op.create_table('issues',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('slug', sa.Text(), nullable=False),
    sa.Column('info', sa.Text(), nullable=False),
    sa.Column('long_info', sa.Text(), nullable=False),
    sa.Column('date', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('lang_uid', sa.Integer(), nullable=True),
    sa.Column('is_disabled', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['lang_uid'], ['languages.uid'], ),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('textversions',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('is_disabled', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    # sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('statements',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('textversion_uid', sa.Integer(), nullable=True),
    sa.Column('is_startpoint', sa.Boolean(), nullable=False),
    sa.Column('issue_uid', sa.Integer(), nullable=True),
    sa.Column('is_disabled', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['issue_uid'], ['issues.uid'], ),
    sa.ForeignKeyConstraint(['textversion_uid'], ['textversions.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('premisegroups',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )

    op.create_table('arguments',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('premisesgroup_uid', sa.Integer(), nullable=True),
    sa.Column('conclusion_uid', sa.Integer(), nullable=True),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('is_supportive', sa.Boolean(), nullable=False),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('issue_uid', sa.Integer(), nullable=True),
    sa.Column('is_disabled', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['conclusion_uid'], ['statements.uid'], ),
    sa.ForeignKeyConstraint(['issue_uid'], ['issues.uid'], ),
    sa.ForeignKeyConstraint(['premisesgroup_uid'], ['premisegroups.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('review_split',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('detector_uid', sa.Integer(), nullable=True),
    sa.Column('premisesgroup_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('is_executed', sa.Boolean(), nullable=False),
    sa.Column('is_revoked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['detector_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['premisesgroup_uid'], ['premisegroups.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )

    op.create_table('arguments_added_by_premisegroups_split',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['review_uid'], ['review_split.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('clicked_arguments',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('is_up_vote', sa.Boolean(), nullable=False),
    sa.Column('is_valid', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('clicked_statements',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('is_up_vote', sa.Boolean(), nullable=False),
    sa.Column('is_valid', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('history',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('path', sa.Text(), nullable=False),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('review_delete_reasons',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reason', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('reason')
    )
    op.create_table('review_deletes',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('detector_uid', sa.Integer(), nullable=True),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('is_executed', sa.Boolean(), nullable=False),
    sa.Column('reason_uid', sa.Integer(), nullable=True),
    sa.Column('is_revoked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['detector_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['reason_uid'], ['review_delete_reasons.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('review_duplicates',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('detector_uid', sa.Integer(), nullable=True),
    sa.Column('duplicate_statement_uid', sa.Integer(), nullable=True),
    sa.Column('original_statement_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('is_executed', sa.Boolean(), nullable=False),
    sa.Column('is_revoked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['detector_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['duplicate_statement_uid'], ['statements.uid'], ),
    sa.ForeignKeyConstraint(['original_statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('review_edits',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('detector_uid', sa.Integer(), nullable=True),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('is_executed', sa.Boolean(), nullable=False),
    sa.Column('is_revoked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['detector_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('review_edit_values',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('review_edit_uid', sa.Integer(), nullable=True),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('typeof', sa.Text(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['review_edit_uid'], ['review_edits.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('review_merge',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('detector_uid', sa.Integer(), nullable=True),
    sa.Column('premisesgroup_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('is_executed', sa.Boolean(), nullable=False),
    sa.Column('is_revoked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['detector_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['premisesgroup_uid'], ['premisegroups.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('review_merge_values',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['review_uid'], ['review_merge.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )

    op.create_table('review_optimizations',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('detector_uid', sa.Integer(), nullable=True),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('is_executed', sa.Boolean(), nullable=False),
    sa.Column('is_revoked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['detector_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )

    op.create_table('review_split_values',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['review_uid'], ['review_split.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )


    op.create_table('marked_statements',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('messages',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('from_author_uid', sa.Integer(), nullable=True),
    sa.Column('to_author_uid', sa.Integer(), nullable=True),
    sa.Column('topic', sa.Text(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('read', sa.Boolean(), nullable=False),
    sa.Column('is_inbox', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['from_author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['to_author_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('optimization_review_locks',
    sa.Column('author_uid', sa.Integer(), nullable=False),
    sa.Column('review_optimization_uid', sa.Integer(), nullable=True),
    sa.Column('locked_since', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['review_optimization_uid'], ['review_optimizations.uid'], ),
    sa.PrimaryKeyConstraint('author_uid')
    )

    op.create_table('premisegroup_merged',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('old_premisegroup_uid', sa.Integer(), nullable=True),
    sa.Column('new_premisegroup_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['new_premisegroup_uid'], ['premisegroups.uid'], ),
    sa.ForeignKeyConstraint(['old_premisegroup_uid'], ['premisegroups.uid'], ),
    sa.ForeignKeyConstraint(['review_uid'], ['review_merge.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('premisegroup_splitted',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('old_premisegroup_uid', sa.Integer(), nullable=True),
    sa.Column('new_premisegroup_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['new_premisegroup_uid'], ['premisegroups.uid'], ),
    sa.ForeignKeyConstraint(['old_premisegroup_uid'], ['premisegroups.uid'], ),
    sa.ForeignKeyConstraint(['review_uid'], ['review_split.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )

    op.create_table('premises',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('premisesgroup_uid', sa.Integer(), nullable=True),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('is_negated', sa.Boolean(), nullable=False),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('issue_uid', sa.Integer(), nullable=True),
    sa.Column('is_disabled', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['issue_uid'], ['issues.uid'], ),
    sa.ForeignKeyConstraint(['premisesgroup_uid'], ['premisegroups.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('reputation_reasons',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reason', sa.Text(), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('reason')
    )
    op.create_table('reputation_history',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reputator_uid', sa.Integer(), nullable=True),
    sa.Column('reputation_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['reputation_uid'], ['reputation_reasons.uid'], ),
    sa.ForeignKeyConstraint(['reputator_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )


    op.create_table('revoked_content',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('revoked_content_history',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('old_author_uid', sa.Integer(), nullable=True),
    sa.Column('new_author_uid', sa.Integer(), nullable=True),
    sa.Column('textversion_uid', sa.Integer(), nullable=True),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['new_author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['old_author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['textversion_uid'], ['textversions.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('revoked_duplicate',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('bend_position', sa.Boolean(), nullable=False),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('premise_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['premise_uid'], ['premises.uid'], ),
    sa.ForeignKeyConstraint(['review_uid'], ['review_duplicates.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('rss',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('issue_uid', sa.Integer(), nullable=True),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['issue_uid'], ['issues.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('seen_arguments',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('user_uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['user_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('seen_statements',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('statement_uid', sa.Integer(), nullable=True),
    sa.Column('user_uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.ForeignKeyConstraint(['user_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('settings',
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('should_send_mails', sa.Boolean(), nullable=False),
    sa.Column('should_send_notifications', sa.Boolean(), nullable=False),
    sa.Column('should_show_public_nickname', sa.Boolean(), nullable=False),
    sa.Column('last_topic_uid', sa.Integer(), nullable=False),
    sa.Column('lang_uid', sa.Integer(), nullable=True),
    sa.Column('keep_logged_in', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['lang_uid'], ['languages.uid'], ),
    sa.ForeignKeyConstraint(['last_topic_uid'], ['issues.uid'], ),
    sa.PrimaryKeyConstraint('author_uid')
    )
    op.create_table('statement_references',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reference', sa.Text(), nullable=False),
    sa.Column('host', sa.Text(), nullable=False),
    sa.Column('path', sa.Text(), nullable=False),
    sa.Column('author_uid', sa.Integer(), nullable=False),
    sa.Column('statement_uid', sa.Integer(), nullable=False),
    sa.Column('issue_uid', sa.Integer(), nullable=False),
    sa.Column('created', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['issue_uid'], ['issues.uid'], ),
    sa.ForeignKeyConstraint(['statement_uid'], ['statements.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('statement_replacements_by_premisegroup_split',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('old_statement_uid', sa.Integer(), nullable=True),
    sa.Column('new_statement_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['new_statement_uid'], ['statements.uid'], ),
    sa.ForeignKeyConstraint(['old_statement_uid'], ['statements.uid'], ),
    sa.ForeignKeyConstraint(['review_uid'], ['review_split.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('statement_replacements_by_premisegroups_merge',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('old_statement_uid', sa.Integer(), nullable=True),
    sa.Column('new_statement_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['new_statement_uid'], ['statements.uid'], ),
    sa.ForeignKeyConstraint(['old_statement_uid'], ['statements.uid'], ),
    sa.ForeignKeyConstraint(['review_uid'], ['review_split.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('review_canceled',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('review_edit_uid', sa.Integer(), nullable=True),
    sa.Column('review_delete_uid', sa.Integer(), nullable=True),
    sa.Column('review_optimization_uid', sa.Integer(), nullable=True),
    sa.Column('review_duplicate_uid', sa.Integer(), nullable=True),
    sa.Column('review_merge_uid', sa.Integer(), nullable=True),
    sa.Column('review_split_uid', sa.Integer(), nullable=True),
    sa.Column('was_ongoing', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.ForeignKeyConstraint(['review_delete_uid'], ['review_deletes.uid'], ),
    sa.ForeignKeyConstraint(['review_duplicate_uid'], ['review_duplicates.uid'], ),
    sa.ForeignKeyConstraint(['review_edit_uid'], ['review_edits.uid'], ),
    sa.ForeignKeyConstraint(['review_merge_uid'], ['review_merge.uid'], ),
    sa.ForeignKeyConstraint(['review_optimization_uid'], ['review_optimizations.uid'], ),
    sa.ForeignKeyConstraint(['review_split_uid'], ['review_split.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('last_reviewers_delete',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reviewer_uid', sa.Integer(), nullable=True),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('is_okay', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['review_uid'], ['review_deletes.uid'], ),
    sa.ForeignKeyConstraint(['reviewer_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('last_reviewers_duplicates',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reviewer_uid', sa.Integer(), nullable=True),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('is_okay', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['review_uid'], ['review_duplicates.uid'], ),
    sa.ForeignKeyConstraint(['reviewer_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('last_reviewers_edit',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reviewer_uid', sa.Integer(), nullable=True),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('is_okay', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['review_uid'], ['review_edits.uid'], ),
    sa.ForeignKeyConstraint(['reviewer_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('last_reviewers_merge',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reviewer_uid', sa.Integer(), nullable=True),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('should_merge', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['review_uid'], ['review_merge.uid'], ),
    sa.ForeignKeyConstraint(['reviewer_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('last_reviewers_optimization',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reviewer_uid', sa.Integer(), nullable=True),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('is_okay', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['review_uid'], ['review_optimizations.uid'], ),
    sa.ForeignKeyConstraint(['reviewer_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('last_reviewers_split',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('reviewer_uid', sa.Integer(), nullable=True),
    sa.Column('review_uid', sa.Integer(), nullable=True),
    sa.Column('should_split', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['review_uid'], ['review_split.uid'], ),
    sa.ForeignKeyConstraint(['reviewer_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('marked_arguments',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('argument_uid', sa.Integer(), nullable=True),
    sa.Column('author_uid', sa.Integer(), nullable=True),
    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.ForeignKeyConstraint(['argument_uid'], ['arguments.uid'], ),
    sa.ForeignKeyConstraint(['author_uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_table('statement_replacements_by_premisegroups_merge')
    op.drop_table('statement_replacements_by_premisegroup_split')
    op.drop_table('statement_references')
    op.drop_table('settings')
    op.drop_table('seen_statements')
    op.drop_table('seen_arguments')
    op.drop_table('rss')
    op.drop_table('revoked_duplicate')
    op.drop_table('revoked_content_history')
    op.drop_table('revoked_content')

    op.drop_table('reputation_history')
    op.drop_table('reputation_reasons')
    op.drop_table('premises')

    op.drop_table('premisegroup_splitted')
    op.drop_table('premisegroup_merged')
    op.drop_table('optimization_review_locks')
    op.drop_table('messages')
    op.drop_table('marked_statements')
    op.drop_table('marked_arguments')
    op.drop_table('last_reviewers_split')
    op.drop_table('last_reviewers_optimization')
    op.drop_table('last_reviewers_merge')
    op.drop_table('last_reviewers_edit')
    op.drop_table('last_reviewers_duplicates')
    op.drop_table('last_reviewers_delete')



    op.drop_table('clicked_statements')
    op.drop_table('clicked_arguments')
    op.drop_table('arguments_added_by_premisegroups_split')

    op.drop_table('review_canceled')
    op.drop_table('review_split_values')
    op.drop_table('review_split')
    op.drop_table('review_optimizations')
    op.drop_table('review_merge_values')
    op.drop_table('review_merge')
    op.drop_table('review_edit_values')
    op.drop_table('review_edits')
    op.drop_table('review_duplicates')
    op.drop_table('review_deletes')
    op.drop_table('review_delete_reasons')


    op.drop_table('arguments')
    op.drop_table('premisegroups')
    op.drop_table('statements')
    op.drop_table('textversions')
    op.drop_table('history')
    op.drop_table('issues')
    op.drop_table('languages')
    op.drop_table('users')
    op.drop_table('groups')
    # ### end Alembic commands ###
